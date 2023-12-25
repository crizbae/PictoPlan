import React from 'react';
import logo from '../assets/logo.png';

const HomePage: React.FunctionComponent = () => {
    return (
        <div>
            <h1>Welcome to our site</h1>
            <p>
                PictoPlan is an innovative web-based platform designed for educators to simplify the process of generating lesson plans from books or textbooks. It automates the traditionally time-consuming task of converting physical books into educational material, allowing teachers to focus on teaching rather than manual content creation.
            </p>
            <p>
                With PictoPlan, you can effortlessly upload pictures from books or textbooks, and our system will automatically generate lesson plans tailored to the content, saving you valuable time and ensuring a consistent, high-quality educational experience.
            </p>
            <img src={logo} alt="Logo" className="logo" />
        </div>
    );
};

export default HomePage;