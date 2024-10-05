import { useProducts } from './useProducts';
import type { Product } from '../types';

describe('useProducts hook', () => {
  it('should return unique product IDs', () => {
    const ids = useProducts().map(p => p.id);
    expect(new Set(ids).size).toBe(ids.length);
  });

  it('should return an array of products', () => {
    const products = useProducts();
    expect(Array.isArray(products)).toBeTruthy();
    expect(products.length).toBe(4);
  });

  it('should return products with correct properties', () => {
    const product = useProducts()[0];
    expect(product.id).toBe(1);
    expect(product.name).toBe('IPhone 14 Pro');
    expect(product.description).toBe('Latest iphone, buy it now');
    expect(product.price).toBe(999);
    expect(product.priceSymbol).toBe('$');
    expect(product.category).toBe('Электроника');
    expect(typeof product.imgUrl).toBe('string');
  });
});
