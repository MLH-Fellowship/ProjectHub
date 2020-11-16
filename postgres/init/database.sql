CREATE TABLE IF NOT EXISTS "HelloWorld" (
	"id" serial,
	"motd" text,
	PRIMARY KEY( id )
);

INSERT INTO "HelloWorld" (motd) VALUES("Drink wine not water.");