import React, { useState, useEffect } from 'react';
import { View, FlatList, Text, Button, StyleSheet } from 'react-native';
import axios from 'axios';
import ProductListItem from '../components/ProductListItem';

const API_BASE_URL = 'http://192.168.0.159:8000/api/data/';

const ProductListScreen = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}products/`);
        setProducts(response.data);
      } catch (error) {
        console.error('Erro ao buscar produtos:', error);
      }
    };

    fetchProducts();
  }, []);

  const handleDeleteProduct = async (productId) => {
    try {
      await axios.delete(`${API_BASE_URL}product/${productId}/`);
      const updatedProducts = products.filter((product) => product.id_product !== productId);
      setProducts(updatedProducts);
    } catch (error) {
      console.error('Erro ao deletar produto:', error);
    }
  };

  const renderItem = ({ item }) => (
    <ProductListItem
      product={item}
      onDelete={() => handleDeleteProduct(item.id_product)}
    />
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={products}
        keyExtractor={(item) => item.id_product.toString()}
        renderItem={renderItem}
        ListEmptyComponent={<Text>Nenhum produto encontrado.</Text>}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
  },
});

export default ProductListScreen;
