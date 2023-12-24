import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import App from './App.tsx'
import Home from './pages/Home.tsx'
import CreatePlan from './pages/CreatePlan.tsx'
import MyPlans from './pages/MyPlans.tsx'
import Gallery from './pages/Gallery.tsx'
import Profile from './pages/Profile.tsx'
import './index.css'

const router = createBrowserRouter([
    {
        path: '/',
        element: <App />,
        errorElement: <h1>Error Route Not Found</h1>,
        children: [
            {
                errorElement: <h1>Error Route Not Found</h1>,
                children: [
                    {
                        path: '/',
                        element: <Home />,
                    },
                    {
                        path: '/createPlan',
                        element: <CreatePlan />,
                    },
                    {
                        path: '/myPlans',
                        element: <MyPlans />,
                    },
                    {
                        path: '/gallery',
                        element: <Gallery />,
                    },
                    {
                        path: '/profile',
                        element: <Profile />,
                    },
                ]
            }
        ],
    },
])

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <RouterProvider router={router} />
    </React.StrictMode>,
)
