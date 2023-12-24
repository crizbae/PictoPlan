import React from 'react'
import { Outlet } from 'react-router-dom'
import Sidebar from './components/Sidebar'
import './App.css'

const App: React.FunctionComponent = () => {

    return (
        <div className="container">
            <Sidebar />
            <div className="content">
                <Outlet />
            </div>
        </div>
    )
}
export default App
