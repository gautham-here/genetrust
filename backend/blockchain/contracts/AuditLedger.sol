// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title AuditLedger
/// @notice Append-only on-chain audit log for all governance events.
///         Provides the "Immutable event trail" lane in the GeneTrust pipeline.
contract AuditLedger {

    // ── Event types (mirrors backend EventType enum) ──────────────────────────
    uint8 public constant EVT_UPLOAD       = 1;
    uint8 public constant EVT_ACCESS       = 2;
    uint8 public constant EVT_AI_ANALYSIS  = 3;
    uint8 public constant EVT_CONSENT      = 4;
    uint8 public constant EVT_REVOCATION   = 5;
    uint8 public constant EVT_ROLE_CHANGE  = 6;
    uint8 public constant EVT_ANOMALY      = 7;
    uint8 public constant EVT_EXPORT       = 8;

    struct AuditEntry {
        bytes32 recordId;      // linked genome record (may be 0 for system events)
        address actor;         // wallet that triggered the event
        uint8   eventType;
        bytes32 dataHash;      // hash of event payload (stored off-chain, verified here)
        uint256 timestamp;
        string  description;   // short human-readable label (no PII)
    }

    // Sequential log — append-only
    AuditEntry[] private ledger;

    // recordId => indices into ledger[] for quick lookup
    mapping(bytes32 => uint256[]) private recordAuditIndex;

    // ── Events ────────────────────────────────────────────────────────────────
    event AuditLogged(
        uint256 indexed entryIndex,
        bytes32 indexed recordId,
        address indexed actor,
        uint8   eventType,
        uint256 timestamp
    );

    // ── Write ─────────────────────────────────────────────────────────────────

    /// @notice Append an audit entry.
    /// @param recordId    Linked genome record (bytes32(0) for system-level events).
    /// @param eventType   One of the EVT_* constants above.
    /// @param dataHash    SHA-256 of the full event JSON stored in your off-chain DB.
    /// @param description Short label, e.g. "Risk analysis completed".
    /// @return index      Position of the new entry in the ledger array.
    function log(
        bytes32 recordId,
        uint8   eventType,
        bytes32 dataHash,
        string calldata description
    ) external returns (uint256 index) {
        require(eventType >= 1 && eventType <= 8, "AuditLedger: unknown event type");
        require(dataHash != bytes32(0), "AuditLedger: empty data hash");

        index = ledger.length;
        ledger.push(AuditEntry({
            recordId:    recordId,
            actor:       msg.sender,
            eventType:   eventType,
            dataHash:    dataHash,
            timestamp:   block.timestamp,
            description: description
        }));

        if (recordId != bytes32(0)) {
            recordAuditIndex[recordId].push(index);
        }

        emit AuditLogged(index, recordId, msg.sender, eventType, block.timestamp);
    }

    // ── Read ──────────────────────────────────────────────────────────────────

    /// @notice Total number of audit entries.
    function totalEntries() external view returns (uint256) {
        return ledger.length;
    }

    /// @notice Fetch a single audit entry by index.
    function getEntry(uint256 index)
        external view
        returns (
            bytes32 recordId,
            address actor,
            uint8   eventType,
            bytes32 dataHash,
            uint256 timestamp,
            string memory description
        )
    {
        require(index < ledger.length, "AuditLedger: index out of bounds");
        AuditEntry storage e = ledger[index];
        return (e.recordId, e.actor, e.eventType, e.dataHash, e.timestamp, e.description);
    }

    /// @notice Fetch all audit entry indices associated with a genome record.
    function getEntriesForRecord(bytes32 recordId)
        external view
        returns (uint256[] memory)
    {
        return recordAuditIndex[recordId];
    }

    /// @notice Verify that a stored entry's data hash matches expected value.
    ///         Use this from the backend to detect off-chain tampering.
    function verifyEntry(uint256 index, bytes32 expectedHash)
        external view
        returns (bool)
    {
        require(index < ledger.length, "AuditLedger: index out of bounds");
        return ledger[index].dataHash == expectedHash;
    }
}