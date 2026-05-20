import React, { useState, useContext, useEffect } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Image, Alert, ScrollView } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { ProductContext } from '../../App';

export default function FormScreen({ route, navigation }) {
  const { products, setProducts } = useContext(ProductContext);
  const editingProduct = route.params?.product;

  const [nombre, setNombre] = useState('');
  const [precio, setPrecio] = useState('');
  const [cantidad, setCantidad] = useState('');
  const [categoria, setCategoria] = useState('');
  const [imagen, setImagen] = useState(null);

  useEffect(() => {
    if (editingProduct) {
      setNombre(editingProduct.nombre);
      setPrecio(editingProduct.precio.toString());
      setCantidad(editingProduct.cantidad.toString());
      setCategoria(editingProduct.categoria);
      setImagen(editingProduct.imagen);
    }
  }, [editingProduct]);

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.Images,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    });

    if (!result.canceled) {
      setImagen(result.assets[0].uri);
    }
  };

  const handleSave = () => {
    if (!nombre.trim() || !precio.trim() || !cantidad.trim() || !categoria.trim()) {
      Alert.alert('Error', 'Todos los campos de texto son obligatorios.');
      return;
    }

    if (isNaN(precio) || isNaN(cantidad)) {
      Alert.alert('Error', 'Precio y cantidad deben ser valores numéricos.');
      return;
    }

    const newProduct = {
      id: editingProduct ? editingProduct.id : Date.now().toString(),
      nombre: nombre.trim(),
      precio: parseFloat(precio),
      cantidad: parseInt(cantidad, 10),
      categoria: categoria.trim(),
      imagen
    };

    if (editingProduct) {
      setProducts(products.map(p => p.id === editingProduct.id ? newProduct : p));
    } else {
      setProducts([...products, newProduct]);
    }

    navigation.goBack();
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.label}>Nombre del producto</Text>
      <TextInput style={styles.input} value={nombre} onChangeText={setNombre} placeholderTextColor="#888" placeholder="Ej. Laptop HP" />

      <Text style={styles.label}>Precio</Text>
      <TextInput style={styles.input} value={precio} onChangeText={setPrecio} keyboardType="numeric" placeholderTextColor="#888" placeholder="Ej. 15000" />

      <Text style={styles.label}>Cantidad en inventario</Text>
      <TextInput style={styles.input} value={cantidad} onChangeText={setCantidad} keyboardType="numeric" placeholderTextColor="#888" placeholder="Ej. 10" />

      <Text style={styles.label}>Categoría</Text>
      <TextInput style={styles.input} value={categoria} onChangeText={setCategoria} placeholderTextColor="#888" placeholder="Ej. Electrónica" />

      <Text style={styles.label}>Imagen del producto</Text>
      <TouchableOpacity style={styles.imagePicker} onPress={pickImage}>
        {imagen ? (
          <Image source={{ uri: imagen }} style={styles.imagePreview} />
        ) : (
          <Text style={styles.imagePickerText}>Seleccionar Imagen</Text>
        )}
      </TouchableOpacity>

      <TouchableOpacity style={styles.saveButton} onPress={handleSave}>
        <Text style={styles.saveButtonText}>Guardar Producto</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: 20,
  },
  label: {
    color: '#00E5FF',
    fontSize: 14,
    marginBottom: 6,
    fontWeight: '600',
  },
  input: {
    backgroundColor: '#1E1E2A',
    color: '#FFF',
    padding: 14,
    borderRadius: 10,
    fontSize: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#2A2A3A',
  },
  imagePicker: {
    backgroundColor: '#1E1E2A',
    height: 150,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 24,
    borderWidth: 1,
    borderColor: '#2A2A3A',
    overflow: 'hidden',
  },
  imagePickerText: {
    color: '#888',
    fontSize: 16,
  },
  imagePreview: {
    width: '100%',
    height: '100%',
  },
  saveButton: {
    backgroundColor: '#00E5FF',
    padding: 16,
    borderRadius: 10,
    alignItems: 'center',
  },
  saveButtonText: {
    color: '#12121A',
    fontSize: 18,
    fontWeight: 'bold',
  },
});