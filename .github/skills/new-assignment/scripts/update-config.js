const fs = require("fs");
const path = require("path");

const [id, title, description, dueDate, ...extraArgs] = process.argv.slice(2);
const configPath = path.resolve(__dirname, "../../../../config.json");
const config = JSON.parse(fs.readFileSync(configPath, "utf8"));

if (!id || !title || !description || extraArgs.length > 0) {
  console.error(
    'Usage: node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>" [YYYY-MM-DD]',
  );
  process.exit(1);
}

if (dueDate && (!/^\d{4}-\d{2}-\d{2}$/.test(dueDate) || new Date(`${dueDate}T00:00:00Z`).toISOString().slice(0, 10) !== dueDate)) {
  console.error("Error: due date must be a valid date in YYYY-MM-DD format");
  process.exit(1);
}

const assignment = {
  id,
  title,
  description,
  path: `assignments/${id}`,
};

if (dueDate) {
  assignment.dueDate = dueDate;
}

config.assignments.push(assignment);

fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");
console.log(`Added "${title}"${dueDate ? ` (due ${dueDate})` : ""}`);