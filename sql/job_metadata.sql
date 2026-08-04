-- File: sql/job_metadata.sql

CREATE TABLE JobMetadata (
    JobName VARCHAR(100),
    LastRunTime DATETIME,
    Status VARCHAR(50)
);
