import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity, Alert } from 'react-native';

export default function ProductCard({ product, onEdit, onDelete }) {
  const confirmDelete = () => {
    Alert.alert(
      "Eliminar Producto",
      `¿Estás seguro de eliminar ${product.nombre}?`,
      [
        { text: "Cancelar", style: "cancel" },
        { text: "Eliminar", onPress: () => onDelete(product.id), style: "destructive" }
      ]
    );
  };

  return (
    <View style={styles.card}>
      {product.imagen ? (
        <Image source={{ uri: product.imagen }} style={styles.image} />
      ) : (
        <View style={styles.placeholderImage}>
          <Text style={styles.placeholderText}>Sin imagen</Text>
        </View>
      )}
      <View style={styles.infoContainer}>
        <Text style={styles.title}>{product.nombre}</Text>
        <Text style={styles.category}>{product.categoria}</Text>
        <View style={styles.row}>
          <Text style={styles.price}>${parseFloat(product.precio).toFixed(2)}</Text>
          <Text style={styles.stock}>Stock: {product.cantidad}</Text>
        </View>
      </View>
      <View style={styles.actions}>
        <TouchableOpacity style={styles.editButton} onPress={() => onEdit(product)}>
          <Text style={styles.actionText}>Editar</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.deleteButton} onPress={confirmDelete}>
          <Text style={styles.actionText}>Borrar</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#1E1E2A',
    borderRadius: 16,
    marginBottom: 16,
    flexDirection: 'row',
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: '#2A2A3A',
  },
  image: {
    width: 100,
    height: '100%',
    backgroundColor: '#2A2A3A',
  },
  placeholderImage: {
    width: 100,
    height: '100%',
    backgroundColor: '#2A2A3A',
    justifyContent: 'center',
    alignItems: 'center',
  },
  placeholderText: {
    color: '#888',
    fontSize: 12,
  },
  infoContainer: {
    flex: 1,
    padding: 12,
  },
  title: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  category: {
    color: '#00E5FF',
    fontSize: 14,
    marginBottom: 8,
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  price: {
    color: '#4CAF50',
    fontSize: 16,
    fontWeight: 'bold',
  },
  stock: {
    color: '#AAAAAA',
    fontSize: 14,
  },
  actions: {
    justifyContent: 'space-around',
    padding: 8,
    backgroundColor: '#1A1A24',
  },
  editButton: {
    backgroundColor: '#00E5FF',
    padding: 8,
    borderRadius: 8,
    alignItems: 'center',
    marginBottom: 8,
  },
  deleteButton: {
    backgroundColor: '#FF5252',
    padding: 8,
    borderRadius: 8,
    alignItems: 'center',
  },
  actionText: {
    color: '#12121A',
    fontWeight: 'bold',
    fontSize: 12,
  },
});