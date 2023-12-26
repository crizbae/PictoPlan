import React from 'react';
import ImageUploaderContainer from '../components/ImageUploaderContainer.tsx';

const CreatePlan: React.FunctionComponent = () => {
    type Image = { id: string, file: File | null };

    const handleImagesChange = (images: Image[]) => {
        // send API call to backend to create plan
        console.log(images);
    }

    return (
        <div>
            <h1>Create Plan</h1>
            <div style={{
                border: '1px solid black', 
                padding: '10px',
            }}>
                <p>Section 1</p>
            <ImageUploaderContainer onImagesChange={ handleImagesChange }/>
            </div>
        </div>
    );
};

export default CreatePlan;