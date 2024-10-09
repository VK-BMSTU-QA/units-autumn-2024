import React, { useState } from 'react';
import '@testing-library/jest-dom';
import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
// import { useCurrentTime, useProducts } from '../../../hooks';
import { Product } from '../../../types';
// import { Categories } from '../../../components/Categories';

// // Мокаем хуки и компоненты
// jest.mock('../../../hooks', () => ({
//     useCurrentTime: jest.fn(),
//     useProducts: jest.fn(),
// }));

// jest.mock('../../../components/Categories', () => ({
//     Categories: jest.fn(() => <div>Categories component</div>),
//     ProductCard: jest.fn(({ name }) => <div>{name}</div>),
// }));

describe('MainPage', () => {
    const mockProducts: Product[] = [
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
    ];

    beforeEach(() => {
        // (useCurrentTime as jest.Mock).mockReturnValue('12:00');
        // (useProducts as jest.Mock).mockReturnValue(mockProducts);
        jest.spyOn(global.Date, 'now').mockImplementation(() => new Date('2023-10-01T12:00:00Z').getTime());
    });

    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('должен отобразить заголовок и текущее время', () => {
        render(<MainPage />);

        expect(screen.getByText('VK Маркет')).toBeInTheDocument();
        // expect(screen.getByText('12:00')).toBeInTheDocument();
        const timeRegex = /\d{2}:\d{2}:\d{2}/;
        expect(screen.getByText(timeRegex)).toBeInTheDocument();
    });

    // it('должен отобразить компонент Categories', () => {
    //     render(<MainPage />);

    //     expect(screen.getByText('Categories component')).toBeInTheDocument();
    // });

    it('должен отобразить продукты с помощью компонента ProductCard', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });

    it('должен обновлять выбранные категории при нажатии на категорию', () => {
        // const mockOnCategoryClick = jest.fn();

        // (Categories as jest.Mock).mockImplementation(({ onCategoryClick }) => (
        //     <button onClick={() => onCategoryClick('Электроника')}>
        //         Электроника
        //     </button>
        // ));

        render(<MainPage />);

        // Используем getByRole для выбора кнопки с текстом "Электроника"
        // const categoryButton = screen.getByRole('button', {
        //     name: 'Электроника',
        // });

        const categoryButton = screen.getByText('Электроника', { selector: '.categories__badge' });
        fireEvent.click(categoryButton);

        // expect(mockOnCategoryClick).not.toHaveBeenCalled(); // Проверка, что mockOnCategoryClick не вызывается, так как setSelectedCategories внутренний

        // Продукты обновляются после клика по категории
        expect(screen.queryByText('Костюм гуся')).not.toBeInTheDocument();
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
    });

    it('должен отобразить все продукты, если категории не выбраны', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });
});
