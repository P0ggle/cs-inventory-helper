db.createUser({
  user: "testuser",
  pwd: "testuser",
  roles: [
    {
      role: "readWrite",
      db: "testing",
    },
  ],
});

db = new Mongo().getDB("testing");
db.createCollection("testcollection");
