-- This script creates an index idx_name_first_score on the table names.
-- The index is created on the first 1 character of the name column and the score column.

CREATE INDEX idx_name_first_score ON names (name(1), score);
