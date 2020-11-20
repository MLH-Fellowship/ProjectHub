CREATE TABLE IF NOT EXISTS projects(
  id serial primary key,
  owner integer,
  slug text,
  name text,
  description text,
  source text,
  demo text,
  tags text,
  languages text
  -- imported smallint -- if the project came from github
);

CREATE TABLE IF NOT EXISTS users(
  id integer primary key, -- equal to github's ids
  login text,
  name text,
  pods text,
  timezone_offset smallint,
  bio text,
  skills text,
  interests text
);
