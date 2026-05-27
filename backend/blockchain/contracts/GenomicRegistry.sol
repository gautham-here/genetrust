// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @title GenomicRegistry
/// @notice Immutably records SHA-256 genome hashes with ownership and timestamps.
///         No raw genomic data ever touches the chain — only hashes.
contract GenomicRegistry {

    struct GenomeRecord {
        bytes32 genomeHash;      // SHA-256 of the anonymized genome
        address submittedBy;     // wallet of the lab/backend submitter
        uint256 timestamp;       // block timestamp at submission
        string  sampleId;        // opaque internal ID (no PII)
        bool    revoked;         // soft-delete / consent withdrawal
    }

    // recordId => GenomeRecord
    mapping(bytes32 => GenomeRecord) private records;

    // submitter => list of recordIds they own
    mapping(address => bytes32[]) private submitterRecords;

    event GenomeRegistered(
        bytes32 indexed recordId,
        bytes32 indexed genomeHash,
        address indexed submittedBy,
        uint256 timestamp,
        string  sampleId
    );

    event GenomeRevoked(
        bytes32 indexed recordId,
        address indexed revokedBy,
        uint256 timestamp
    );

    /// @notice Register a new genome hash on-chain.
    /// @param genomeHash  SHA-256 hash of the anonymized genomic payload.
    /// @param sampleId    Internal opaque sample identifier (no PII).
    /// @return recordId   Unique on-chain record ID derived from hash + sender + time.
    function registerGenome(
        bytes32 genomeHash,
        string calldata sampleId
    ) external returns (bytes32 recordId) {
        require(genomeHash != bytes32(0), "GenomicRegistry: empty hash");
        require(bytes(sampleId).length > 0, "GenomicRegistry: empty sampleId");

        recordId = keccak256(
            abi.encodePacked(genomeHash, msg.sender, block.timestamp)
        );
        require(
            records[recordId].timestamp == 0,
            "GenomicRegistry: record already exists"
        );

        records[recordId] = GenomeRecord({
            genomeHash:  genomeHash,
            submittedBy: msg.sender,
            timestamp:   block.timestamp,
            sampleId:    sampleId,
            revoked:     false
        });
        submitterRecords[msg.sender].push(recordId);

        emit GenomeRegistered(recordId, genomeHash, msg.sender, block.timestamp, sampleId);
    }

    /// @notice Revoke a genome record (consent withdrawal / error correction).
    ///         Only the original submitter can revoke.
    function revokeGenome(bytes32 recordId) external {
        GenomeRecord storage rec = records[recordId];
        require(rec.timestamp != 0, "GenomicRegistry: record not found");
        require(rec.submittedBy == msg.sender, "GenomicRegistry: not owner");
        require(!rec.revoked, "GenomicRegistry: already revoked");

        rec.revoked = true;
        emit GenomeRevoked(recordId, msg.sender, block.timestamp);
    }

    /// @notice Verify that a genome hash matches a stored record.
    /// @return valid      True if the hash matches and is not revoked.
    /// @return timestamp  When the record was registered (0 if not found).
    function verifyGenome(
        bytes32 recordId,
        bytes32 genomeHash
    ) external view returns (bool valid, uint256 timestamp) {
        GenomeRecord storage rec = records[recordId];
        valid = (rec.genomeHash == genomeHash && !rec.revoked);
        timestamp = rec.timestamp;
    }

    /// @notice Fetch the full record for a given recordId.
    function getRecord(bytes32 recordId)
        external view
        returns (
            bytes32 genomeHash,
            address submittedBy,
            uint256 timestamp,
            string memory sampleId,
            bool revoked
        )
    {
        GenomeRecord storage rec = records[recordId];
        require(rec.timestamp != 0, "GenomicRegistry: record not found");
        return (rec.genomeHash, rec.submittedBy, rec.timestamp, rec.sampleId, rec.revoked);
    }

    /// @notice List all recordIds submitted by a given address.
    function getRecordsBySubmitter(address submitter)
        external view
        returns (bytes32[] memory)
    {
        return submitterRecords[submitter];
    }
}