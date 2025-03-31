import React, { useState } from 'react';
import axios from 'axios';
import { useForm } from "react-hook-form";

export default function UploadForm() {
    const { register, handleSubmit, reset } = useForm();
    const [loading, setLoading] = useState(false);
    
    const submit = async (data) => {
        const formData = new FormData();
        formData.append('file', data.file[0]);
        formData.append('class_type', data.class_type);
        formData.append('subject', data.subject);
        formData.append('chapter_name', data.chapter_name);
        
        setLoading(true);
        try {
            const response = await axios.post('http://127.0.0.1:8000/upload/', formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
            });
            console.log('Response from backend:', response.data);
            alert('File uploaded successfully!');
            reset(); // Reset form after successful submission
        } catch (error) {
            console.error('Error uploading file:', error);
            alert('Failed to upload file.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: '20px', maxWidth: '400px', margin: 'auto' }}>
            <form onSubmit={handleSubmit(submit)} encType="multipart/form-data">
                <label>Class:</label>
                <input
                    type="number"
                    {...register("class_type", { required: true })}
                /><br />
                
                <label>Subject:</label>
                <input
                    type="text"
                    {...register("subject", { required: true })}
                /><br />
                
                <label>Chapter Name:</label>
                <input
                    type="text"
                    {...register("chapter_name", { required: true })}
                /><br />
                
                <label>Browse File:</label>
                <input
                    type="file"
                    {...register("file", { required: true })}
                /><br />
                
                <button type="submit" disabled={loading}>
                    {loading ? 'Uploading...' : 'Submit'}
                </button>
            </form>
        </div>
    );
}
