import React, { useState, useRef, useEffect } from 'react'
import { FaTrash } from 'react-icons/fa';

interface ImageUploaderProps {
    onFileChange?: (file: File | null) => void;
}

const ImageUploader: React.FunctionComponent<ImageUploaderProps> = ({ onFileChange }) => {
    const [imagePreview, setImagePreview] = useState<string | null>(null);
    const fileInputRef = useRef<HTMLInputElement>(null);

    useEffect(() => {
        return () => {
            if (imagePreview) {
                URL.revokeObjectURL(imagePreview);
            }
        };
    }, [imagePreview]);

    const handleFile = (file: File | null) => {
        if (file) {
            setImagePreview(URL.createObjectURL(file));
            if (onFileChange) {
                onFileChange(file);
            }
        }
    }

    const handleDragOver = (event: React.DragEvent<HTMLDivElement>) => {
        event.preventDefault()
    }

    const handleOnDrop = (event: React.DragEvent<HTMLDivElement>) => {
        const imageFile = event.dataTransfer.files[0];
        handleFile(imageFile);
        event.preventDefault();
    }

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files ? event.target.files[0] : null;
        handleFile(file);
    }

    const handleClick = () => {
        fileInputRef.current?.click();
    }

    const handleDelete = () => {
        setImagePreview(null);
        if (onFileChange) {
            onFileChange(null);
        }
    }

    return (
        <div className="image-uploader">
            {
                imagePreview ? (
                    <div className='preview'>
                        <img src={imagePreview} alt='Preview of Image' />
                        <button onClick={handleDelete} style={{
                            position: 'absolute',
                            top: '10px',
                            right: '10px',
                            padding: '5px',
                        }}>
                            <FaTrash style={{ color: '#b30000' }} />
                        </button>
                    </div>
                ) : (
                    <div className='preview'>
                        <input type="file" ref={fileInputRef} onChange={handleFileChange} style={{ display: 'none' }} />
                        <div className='drop-zone' onDragOver={handleDragOver} onDrop={handleOnDrop} onClick={handleClick}>
                            <p>Drag and drop image here...</p>
                        </div>
                    </div>
                )
            }
        </div>
    )
}
export default ImageUploader