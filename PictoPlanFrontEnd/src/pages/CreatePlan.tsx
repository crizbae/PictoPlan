import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';
import ImageUploaderContainer from '../components/ImageUploaderContainer.tsx';
import { useNavigate } from "react-router-dom";

const CreatePlan: React.FunctionComponent = () => {
    type Image = { id: string, file: File | null };

    const [sections, setSection] = useState<Image[][]>([[]]);
    const navigate = useNavigate();

    const handleImagesChange = (section: number) => (images: Image[]) => {
        const newSections = [...sections];
        newSections[section] = images;
        setSection(newSections);
    }

    const submitPlans = () => {
        // create image names in a dict with: uuid-section#-image#
        // then convert to base64
        // then send to backend
        const session_uuid = uuidv4().replace(/-/g, '');
        const imageDict: { [key: string]: string | undefined }  = {};
        // remove null images from sections
        sections.forEach((section, sectionIndex) => {
            sections[sectionIndex] = section.filter((image) => image.file !== null);
        });
        sections.forEach((section, sectionIndex) => {
            section.forEach((image, imageIndex) => {
                // convert file to base64 using FileReader and readAsDataURL
                const reader = new FileReader();
                if (image.file) {
                    reader.readAsDataURL(image.file);
                    reader.onloadend = () => {
                        const base64data = reader.result?.toString().split(',')[1];
                        imageDict[`${session_uuid}-${sectionIndex + 1}-${imageIndex + 1}`] = base64data;
                    }
                }
            });
        });
        // now send imageDict to backend
        console.log(imageDict);

        // redirect to session page 'plan page' with session_uuid using useNavigate
        navigate(`/myplans?plan=${session_uuid}`);
    }

    return (
        <div>
            <h1>Create Plan</h1>
            <button onClick={() => submitPlans()}>Submit Plans</button>
            {
                sections.map((_, i) => (
                    <div key={i} style={{
                        border: '1px solid black',
                        padding: '1rem',
                        margin: '1rem',
                    }}>
                        <p>Section {i + 1}</p>
                        <ImageUploaderContainer onImagesChange={ handleImagesChange(i) }/>
                    </div>
                ))
            }
            <div>
                <button onClick={() => setSection([...sections, []])}>Add Section</button>
            </div>
        </div>
        
    );
};

export default CreatePlan;