// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title AccessPolicy
/// @notice Manages on-chain consent and role-based access for genome records.
///         Mirrors the off-chain RBAC layer with a tamper-proof on-chain record.
contract AccessPolicy {

    // ── Roles ────────────────────────────────────────────────────────────────
    uint8 public constant ROLE_NONE    = 0;
    uint8 public constant ROLE_PATIENT = 1;
    uint8 public constant ROLE_LAB     = 2;
    uint8 public constant ROLE_ADMIN   = 3;

    struct Policy {
        address owner;           // patient / primary data subject
        bool    consentGiven;    // explicit consent flag
        uint256 consentTimestamp;
        mapping(address => uint8) roleGrants; // grantee => role
    }

    // recordId => Policy
    mapping(bytes32 => Policy) private policies;

    // ── Events ────────────────────────────────────────────────────────────────
    event PolicyCreated(bytes32 indexed recordId, address indexed owner);
    event ConsentToggled(bytes32 indexed recordId, address indexed owner, bool consent);
    event RoleGranted(bytes32 indexed recordId, address indexed grantee, uint8 role);
    event RoleRevoked(bytes32 indexed recordId, address indexed grantee);

    // ── Modifiers ─────────────────────────────────────────────────────────────
    modifier onlyOwner(bytes32 recordId) {
        require(policies[recordId].owner == msg.sender, "AccessPolicy: not owner");
        _;
    }

    modifier policyExists(bytes32 recordId) {
        require(policies[recordId].owner != address(0), "AccessPolicy: no policy");
        _;
    }

    // ── Core functions ────────────────────────────────────────────────────────

    /// @notice Create an access policy for a genome record.
    ///         Called by the backend wallet immediately after GenomicRegistry.registerGenome.
    /// @param recordId   The on-chain record ID from GenomicRegistry.
    /// @param owner      The patient's wallet (or a custody address representing them).
    function createPolicy(bytes32 recordId, address owner) external {
        require(owner != address(0), "AccessPolicy: zero owner");
        require(policies[recordId].owner == address(0), "AccessPolicy: policy exists");

        policies[recordId].owner = owner;
        policies[recordId].consentGiven = false;
        emit PolicyCreated(recordId, owner);
    }

    /// @notice Patient grants or withdraws consent for their record.
    function setConsent(bytes32 recordId, bool consent)
        external
        policyExists(recordId)
        onlyOwner(recordId)
    {
        policies[recordId].consentGiven = consent;
        if (consent) {
            policies[recordId].consentTimestamp = block.timestamp;
        }
        emit ConsentToggled(recordId, msg.sender, consent);
    }

    /// @notice Owner grants a role to an address (lab technician, clinician, etc.)
    function grantRole(bytes32 recordId, address grantee, uint8 role)
        external
        policyExists(recordId)
        onlyOwner(recordId)
    {
        require(role >= ROLE_PATIENT && role <= ROLE_ADMIN, "AccessPolicy: invalid role");
        require(grantee != address(0), "AccessPolicy: zero grantee");

        policies[recordId].roleGrants[grantee] = role;
        emit RoleGranted(recordId, grantee, role);
    }

    /// @notice Owner revokes all access for a grantee.
    function revokeRole(bytes32 recordId, address grantee)
        external
        policyExists(recordId)
        onlyOwner(recordId)
    {
        policies[recordId].roleGrants[grantee] = ROLE_NONE;
        emit RoleRevoked(recordId, grantee);
    }

    /// @notice Check whether an address is authorised to access a record.
    /// @return authorised  True if consent is given AND the caller has a role >= minRole.
    function isAuthorised(bytes32 recordId, address caller, uint8 minRole)
        external view
        policyExists(recordId)
        returns (bool authorised)
    {
        Policy storage p = policies[recordId];
        if (!p.consentGiven) return false;
        if (p.owner == caller)  return true;   // owner always has access
        return p.roleGrants[caller] >= minRole;
    }

    /// @notice Read the consent status and owner for a record.
    function getPolicyInfo(bytes32 recordId)
        external view
        policyExists(recordId)
        returns (address owner, bool consentGiven, uint256 consentTimestamp)
    {
        Policy storage p = policies[recordId];
        return (p.owner, p.consentGiven, p.consentTimestamp);
    }

    /// @notice Read the role of a specific grantee.
    function getRole(bytes32 recordId, address grantee)
        external view
        policyExists(recordId)
        returns (uint8)
    {
        return policies[recordId].roleGrants[grantee];
    }
}