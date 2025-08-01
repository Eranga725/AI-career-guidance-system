
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'; // Assuming the backend runs on this address

export const getPrediction = async (data: any) => {
  try {
    const response = await axios.post(`${API_URL}/predict`, data);
    return response.data;
  } catch (error) {
    console.error('Error fetching prediction:', error);
    throw error;
  }
};
