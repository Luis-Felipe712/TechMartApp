import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const ProductListItem = ({ product, onDelete }) => {
  return (
    <View style={styles.container}>
      <Text>{product.name}</Text>
      <Text>{product.description}</Text>
      <Text>Price: ${product.price}</Text>
      <Text>Quantity: {product.quantity}</Text>
      <Button title="Delete" onPress={onDelete} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 10,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
  },
});

export default ProductListItem;
