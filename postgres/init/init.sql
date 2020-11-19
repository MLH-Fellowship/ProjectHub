CREATE TABLE IF NOT EXISTS projects(
  id serial primary key,
  name text,
  description text,
  source_link text,
  demo_link text,
  tags text,
  authors text
);

CREATE TABLE IF NOT EXISTS users(
  username text primary key,
  fullname text,
  pods text,
  timezone text,
  bio text,
  skills text,
  interests text
);