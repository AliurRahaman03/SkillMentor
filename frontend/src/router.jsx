// src/router.jsx
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Login from "./pages/Auth/Login";
import Signup from "./pages/Auth/Signup";
import Dashboard from "./pages/Dashboard";
import RoadmapViewer from "./pages/RoadmapViewer";

const router = createBrowserRouter([
  { path: "/", element: <Login /> },
  { path: "/signup", element: <Signup /> },
  { path: "/dashboard", element: <Dashboard /> },
  { path: "/roadmap", element: <RoadmapViewer /> },
]);

export default function AppRouter() {
  return <RouterProvider router={router} />;
}
