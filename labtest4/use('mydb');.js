use('mydb');

// Insert sample data
db.students.insertOne({
  name: "Varshitha",
  age: 21,
  course: "B.Tech CSE"
});

// View data
db.students.find();
