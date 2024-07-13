-- This script creates an index idx_name_first on the table names
-- The index is created on the first 1 character of the name column.

CREATE INDEX idx_name_first ON names (name(1));
