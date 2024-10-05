import { renderHook } from '@testing-library/react-hooks';
import { useProducts } from '../useProducts';

describe('useProducts', () => {
  test('возвращает список продуктов', () => {
    const { result } = renderHook(() => useProducts());

    expect(result.current).toHaveLength(4);
    expect(result.current[0]).toEqual({
      id: 1,
      name: 'IPhone 14 Pro',
      description: 'Latest iphone, buy it now',
      price: 999,
      priceSymbol: '$',
      category: 'Электроника',
      imgUrl: '/iphone.png',
    });

    expect(result.current[1]).toEqual({
      id: 2,
      name: 'Костюм гуся',
      description: 'Запускаем гуся, работяги',
      price: 1000,
      priceSymbol: '₽',
      category: 'Одежда',
    });

    expect(result.current[2]).toEqual({
      id: 3,
      name: 'Настольная лампа',
      description: 'Говорят, что ее использовали в pixar',
      price: 699,
      category: 'Для дома',
      imgUrl: '/lamp.png',
    });

    expect(result.current[3]).toEqual({
      id: 4,
      name: 'Принтер',
      description: 'Незаменимая вещь для студента',
      price: 7000,
      category: 'Электроника',
    });
  });
});
