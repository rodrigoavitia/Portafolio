import React, { useContext, useState } from 'react';
import { View, FlatList, TextInput, StyleSheet, TouchableOpacity, Text } from 'react-native';
import { ProductContext } from '../../App';
import ProductCard from '../components/ProductCard';

export default function HomeScreen({ navigation }) {
  const { products, setProducts } = useContext(ProductContext);
  const [search, setSearch] = useState('');

  const handleDelete = (id) => {
    setProducts(products.filter(item => item.id !== id));
  };

  const handleEdit = (product) => {
    navigation.navigate('Form', { product });
  };

  const filteredProducts = products.filter(p => 
    p.nombre.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.searchInput}
        placeholder="Buscar producto por nombre..."
        placeholderTextColor="#888"
        value={search}
        onChangeText={setSearch}
      />
      
      <FlatList
        data={filteredProducts}
        keyExtractor={item => item.id}
        contentContainerStyle={styles.listContainer}
        renderItem={({ item }) => (
          <ProductCard 
            product={item} 
            onEdit={handleEdit} 
            onDelete={handleDelete} 
          />
        )}
        ListEmptyComponent={
          <Text style={styles.emptyText}>No hay productos en el inventario.</Text>
        }
      />

      <TouchableOpacity 
        style={styles.fab} 
        onPress={() => navigation.navigate('Form')}
      >
        <Text style={styles.fabText}>+</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  searchInput: {
    backgroundColor: '#1E1E2A',
    color: '#FFF',
    padding: 16,
    borderRadius: 12,
    fontSize: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#2A2A3A',
  },
  listContainer: {
    paddingBottom: 80,
  },
  emptyText: {
    color: '#888',
    textAlign: 'center',
    marginTop: 40,
    fontSize: 16,
  },
  fab: {
    position: 'absolute',
    bottom: 24,
    right: 24,
    backgroundColor: '#00E5FF',
    width: 60,
    height: 60,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 5,
    shadowColor: '#00E5FF',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
  },
  fabText: {
    color: '#12121A',
    fontSize: 32,
    fontWeight: 'bold',
  },
});