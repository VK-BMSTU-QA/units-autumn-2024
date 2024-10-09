import React, { useState } from 'react';
import { Product } from "../../../types";
import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import { Categories } from '../../../components/Categories';
import '@testing-library/jest-dom';
import { useCurrentTime, useProducts } from '../../../hooks';
import * as updateModule from '../../../utils/updateCategories';
import * as applyModule from '../../../utils/applyCategories';

jest.mock('../../../hooks', () => ({
    useCurrentTime: jest.fn(),
    useProducts: jest.fn(),
}));


const mockUpdate = jest.spyOn(updateModule, 'updateCategories');
const mockApply = jest.spyOn(applyModule, 'applyCategories');

describe('MainPage test', () => {
    const products: Product[] = [
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
        {
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        },
        {
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        },
    ];

    beforeEach(() => {
        (useCurrentTime as jest.Mock).mockReturnValue('14:00');
        (useProducts as jest.Mock).mockReturnValue(products);
    });

    test('должен отображать корректное время', () => {
        render(<MainPage />);

        expect(screen.getByText('14:00')).toBeInTheDocument();
    });

    test('должен отфильтровать продукты при нажатии на категорию', () => {
        render(<MainPage />);
        products.forEach(({ name }) => 
            expect(screen.queryByText(name)).not.toBeNull()
        );
        fireEvent.click(screen.getAllByText('Электроника')[0]);
        products.forEach(({ name, category }) => {
            if(category == 'Электроника') {
            expect(screen.queryByText(name)).not.toBeNull();
            } else {
            expect(screen.queryByText(name)).toBeNull();
            }
        });
    });

    test('должен отобразить продукты с помощью компонента ProductCard', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });

});
