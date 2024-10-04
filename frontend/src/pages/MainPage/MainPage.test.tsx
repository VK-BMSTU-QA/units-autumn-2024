import { MainPage } from './MainPage';
import { render, fireEvent } from '@testing-library/react';
import { useCurrentTime, useProducts } from '../../hooks';
import React from 'react';

jest.mock('../../hooks');

describe('test main page component', () => {
    it('shoulds contain only 1 product with category Electronics', () => {
        jest.mocked(useProducts).mockReturnValue([
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
        ]);

        const rendered = render(<MainPage />);

        expect(rendered.queryAllByText('Электроника').length).toEqual(2);
    });
    it('shoulds contain specified time', () => {
        jest.mocked(useCurrentTime).mockReturnValue('2020-01-01');

        const rendered = render(<MainPage />);

        expect(rendered.queryAllByText('2020-01-01').length).toBeGreaterThan(0);
    });
    it('shoulds click on category', () => {
        const rendered = render(<MainPage />);

        expect(rendered.queryAllByText('Для дома').length).toEqual(2);
        fireEvent.click(rendered.queryAllByText('Одежда')[0]);
        expect(rendered.queryAllByText('Для дома').length).toEqual(1);
    });
});
