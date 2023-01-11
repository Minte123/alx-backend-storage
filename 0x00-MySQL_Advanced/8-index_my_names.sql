-- SQL script that creates an index idx_name_first on the table names and the first letter of name.
alter table names add index idx_name_first (name(1));
