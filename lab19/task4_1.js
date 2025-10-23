// ...existing code...
/**
 * Print each student name from an array.
 * @param {string[]} students
 */
function printStudents(students) {
    if (!Array.isArray(students)) {
        console.error("printStudents: expected an array of names");
        return;
    }
    if (students.length === 0) {
        console.log("No students to print.");
        return;
    }
    students.forEach((name) => console.log(name));
}

module.exports = { printStudents };

// Demo when run directly
if (require.main === module) {
    printStudents(["Alice", "Bob", "Charlie"]);
}
// ...existing code...