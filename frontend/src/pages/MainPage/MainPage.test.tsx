import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

//Мокаем функции utils
jest.mock('../../utils', () => ({
    applyCategories: jest.fn((products, categories) => products),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

//Мокаем хуки
jest.mock('../../hooks', () => ({
    useProducts: jest.fn(() => [
        {
            id: 1,
            name: 'Компьютер',
            description: 'Описание компьютера',
            price: 1000,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: 'img1.png',
        },
        {
            id: 2,
            name: 'Ваза',
            description: 'Описание вазы',
            price: 2000,
            priceSymbol: '$',
            category: 'Для дома',
            imgUrl: 'img2.png',
        },
    ]),
    useCurrentTime: jest.fn(() => '11:00 PM'),
}));

describe('MainPageTest', () => {
    it('should render MainPage correctly', () => {
        const { getByText } = render(<MainPage />);
        expect(getByText('VK Маркет')).toBeInTheDocument();
        expect(getByText('12:00 PM')).toBeInTheDocument();
        expect(getByText('Product 1')).toBeInTheDocument();
        expect(getByText('Product 2')).toBeInTheDocument();
        expect(getByText('100 $')).toBeInTheDocument();
        expect(getByText('200 $')).toBeInTheDocument();
    });
});
