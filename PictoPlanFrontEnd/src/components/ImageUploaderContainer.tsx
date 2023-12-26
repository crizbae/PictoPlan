import React, { useState } from 'react';
import ImageUploader from './ImageUploader.tsx';

type Image = { id: string, file: File | null };

interface ImageUploadersContainerProps {
    onImagesChange: (images: Image[]) => void;
}

const ImageUploaderContainer: React.FunctionComponent<ImageUploadersContainerProps> = ({ onImagesChange }) => {
    const [images, setImages] = useState<Image[]>([]);
    const [draggingId, setDraggingId] = useState<string | null>(null);

    const handleFileChange = (id: string) => (file: File | null) => {
        const newImages = images.map(image => image.id === id ? { ...image, file } : image);
        setImages(newImages);
        onImagesChange(newImages);
    };

    const addImage = () => {
        const newImages = [...images, { id: Date.now().toString(), file: null }];
        setImages(newImages);
        onImagesChange(newImages);
    };

    const moveImage = (fromId: string, toId: string) => {
        const fromIndex = images.findIndex(image => image.id === fromId);
        const toIndex = images.findIndex(image => image.id === toId);
        const newImages = [...images];
        const fromImage = newImages[fromIndex];
        newImages[fromIndex] = newImages[toIndex];
        newImages[toIndex] = fromImage;
        setImages(newImages);
        onImagesChange(newImages);
    }

    const handleDragStart = (id: string) => (event: React.DragEvent<HTMLDivElement>) => {
        setDraggingId(id);
        const target = event.currentTarget.querySelector('img') as HTMLImageElement;
        if (target && event.dataTransfer) {
            const dragImage = new Image();
            dragImage.src = target.src;
            dragImage.width = 200;
            dragImage.height = 200;
            dragImage.onload = () => {
                event.dataTransfer.setDragImage(dragImage, dragImage.width / 2, dragImage.height / 2);
            }
        }
    };

    const handleDrop = (id: string) => {
        if (draggingId === null) {
            return;
        }
        if (draggingId === id) {
            setDraggingId(null);
            return;
        }
        moveImage(draggingId, id);
        setDraggingId(null);
    }

    const handleDragOver = (event: React.DragEvent<HTMLDivElement>) => {
        event.preventDefault();
        event.stopPropagation();
    }

    return (
        <div style={{ display: 'flex', flexWrap: 'wrap' }}>
            {images.map((image, index) => (
                <div
                    style={{
                        display: 'flex',
                        justifyContent: 'center',
                        alignItems: 'center',
                        position: 'relative',
                        width: '200px',
                        height: '200px',
                        margin: '10px',
                        padding: '5px'
                    }}
                    draggable="true"
                    onDragStart={(e) => handleDragStart(image.id)(e)}
                    onDragOver={(e) => handleDragOver(e)}
                    onDrop={() => handleDrop(image.id)}
                    key={image.id}
                >
                    <p className='page-text'>{index + 1}</p>
                    <ImageUploader onFileChange={handleFileChange(image.id)} />
                </div>
            ))}
            <button onClick={addImage}>Add Image</button>
        </div>
    );
};

export default ImageUploaderContainer;