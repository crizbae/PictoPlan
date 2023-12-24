import React from 'react';
import { Link } from 'react-router-dom';
import { SidebarData } from './SidebarData';

const Sidebar: React.FunctionComponent = () => {
    const mainItems = SidebarData.filter(item => item.title !== 'Profile');
    const profileItem = SidebarData.find(item => item.title === 'Profile');

    return (
        <div className="sidebar">
            <ul>
                {mainItems.map((item, index) => {
                    return (
                        <li key={index}>
                            <Link to={item.path} className="sidebar-link">
                                {item.icon}
                                <span className='sidebar-item'>{item.title}</span>
                            </Link>
                        </li>
                    );
                })}
            </ul>
            {profileItem &&
                <ul>
                    <li>
                        <Link to={profileItem.path} className="sidebar-link">
                            {profileItem.icon}
                            <span className='sidebar-item'>{profileItem.title}</span>
                        </Link>
                    </li>
                </ul>
            }
        </div>
    );
};

export default Sidebar;