import axios from 'axios';

const API_BASE_URL = 'http://192.168.0.159:8000/api/data/';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const getProducts = async () => {
  try {
    const response = await api.get('products/');
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const deleteProduct = async (productId) => {
  try {
    await api.delete(`product/${productId}/`);
  } catch (error) {
    throw error;
  }
};

export const createProduct = async (productData) => {
    try {
      const response = await api.post('products/', productData);
      return response.data;
    } catch (error) {
      throw error;
    }
  };
 
  
  