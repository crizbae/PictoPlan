import * as FaIcons from 'react-icons/fa'

export const SidebarData = [
    {
        title: 'Home',
        path: '/',
        icon: <FaIcons.FaHome />,
    },
    {
        title: 'Create Plan',
        path: '/createPlan',
        icon: <FaIcons.FaPlus />,
    },
    {
        title: 'My Plans',
        path: '/myPlans',
        icon: <FaIcons.FaList />,
    },
    {
        title: 'Gallery',
        path: '/gallery',
        icon: <FaIcons.FaImages />,
    },
    {
        title: 'Profile',
        path: '/profile',
        icon: <FaIcons.FaUser />,
    }
]