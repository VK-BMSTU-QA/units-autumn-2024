import React from 'react';
import {fireEvent, render} from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import {updateCategories} from "../../utils";

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
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        },
        {
            id: 2,
            name: 'Костюм гуся',
            description: 'Запускаем гуся, работяги',
            price: 1000,
            priceSymbol: '₽',
            category: 'Одежда',
        },
    ]),
    useCurrentTime: jest.fn(() => '11:00:01'),
}));

describe('MainPageTest', () => {
    it('should render page correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render elements correctly', () => {
        const { container } = render(<MainPage />);
        const header = container.getElementsByClassName('main-page__title');
        const categories =
            container.getElementsByClassName('categories__badge');
        const products = container.getElementsByClassName('product-card');

        expect(header.length).toBe(1);
        expect(categories.length).toBe(3);
        expect(products.length).toBe(2);
    });

    it('should render current time correctly', () => {
        const { getByText } = render(<MainPage />);
        const currentTime = getByText('11:00:01');

        expect(currentTime).toBeInTheDocument();
    });

    it('on click called', () => {
        const rendered = render(<MainPage />);

        const categoryButton = rendered.getByText('Электроника', {
            selector: '.categories__badge',
        });

        expect(updateCategories).toHaveBeenCalledTimes(0);
        expect(categoryButton).not.toHaveClass('categories__badge_selected');

        fireEvent.click(categoryButton);

        expect(updateCategories).toHaveBeenCalledTimes(1);
        expect(categoryButton).toHaveClass('categories__badge_selected');
    });
});
