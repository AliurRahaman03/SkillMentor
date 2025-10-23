import { useEffect, useState } from "react";
import api from "../api/api";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const [skills, setSkills] = useState([]);

  useEffect(() => {
    api.get("/skills").then((res) => setSkills(res.data));
  }, []);

  return (
    <div>
      <h1>My Dashboard</h1>
      <Link to="/roadmap">Generate Roadmap</Link>
      <ul>
        {skills.map((skill) => (
          <li key={skill.id}>
            {skill.name} ({skill.level})
          </li>
        ))}
      </ul>
    </div>
  );
}
