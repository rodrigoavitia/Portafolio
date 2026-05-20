

import React, { useState, createContext } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import HomeScreen from './src/screens/HomeScreen';
import FormScreen from './src/screens/FormScreen';

export const ProductContext = createContext();
const Stack = createNativeStackNavigator();

export default function App() {
  const [products, setProducts] = useState([]);

  return (
    <ProductContext.Provider value={{ products, setProducts }}>
      <NavigationContainer>
        <Stack.Navigator
          screenOptions={{
            headerStyle: { backgroundColor: '#1A1A24' },
            headerTintColor: '#00E5FF',
            headerTitleStyle: { fontWeight: 'bold', fontSize: 22 },
            contentStyle: { backgroundColor: '#12121A' },
            headerShadowVisible: false,
          }}
        >
          <Stack.Screen name="Home" component={HomeScreen} options={{ title: 'Inventario' }} />
          <Stack.Screen name="Form" component={FormScreen} options={{ title: 'Gestión de Producto' }} />
        </Stack.Navigator>
      </NavigationContainer>
    </ProductContext.Provider>
  );
}