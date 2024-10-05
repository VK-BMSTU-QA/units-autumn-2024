import React from 'react';
import { render, fireEvent, act } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useProducts } from '../../hooks';
import { Product } from '../../types';

const products: Product[] = [
    {
        name: 'Iphone',
        description: 'Iphone_desc',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: 'imageUrl_1',
        id: 1,
    },
    {
        name: 'lamp',
        description: 'lamp_desc',
        price: 150,
        priceSymbol: '$',
        category: 'Для дома',
        imgUrl: 'imageUrl',
        id: 2,
    },
];

jest.mock('../../hooks', () => ({
    ...jest.requireActual('../../hooks'),
    useProducts: jest.fn(),
}));

describe('MainPage test', () => {
    let setIntervalSpy: jest.SpyInstance;
    let clearIntervalSpy: jest.SpyInstance;

    beforeEach(() => {
        (useProducts as jest.Mock).mockReturnValue(products);

        jest.useFakeTimers();
        setIntervalSpy = jest.spyOn(global, 'setInterval');
        clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        jest.spyOn(global, 'Date').mockImplementation(
            () =>
                ({
                    toLocaleTimeString: () => '12:00:00',
                } as unknown as Date)
        );
    });

    afterEach(() => {
        jest.clearAllTimers();
        setIntervalSpy.mockRestore();
        clearIntervalSpy.mockRestore();
        (global.Date as unknown as jest.Mock).mockRestore();
    });



    it('should clear the interval on unmount', () => {
        const { unmount } = render(<MainPage />);
        expect(setIntervalSpy).toHaveBeenCalledTimes(1);

        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);
    });

    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call callback when category click', () => {
        const rendered = render(<MainPage />);
        fireEvent.click(rendered.getAllByText('Для дома')[0]);
        expect(rendered.getByText('lamp')).toBeInTheDocument();
    });

    it('should render ProductCard for everything after unselecting all categories', () => {
        const rendered = render(<MainPage />);

        fireEvent.click(rendered.getAllByText('Для дома')[0]);
        fireEvent.click(rendered.getAllByText('Для дома')[0]);
        expect(rendered.getByText('Iphone')).toBeInTheDocument();
        expect(rendered.getByText('lamp')).toBeInTheDocument();
    });

    it('should render ProductCard for electronics', () => {
        const rendered = render(<MainPage />);

        expect(rendered.getByText('lamp')).toBeInTheDocument();
        expect(rendered.getByText('lamp_desc')).toBeInTheDocument();
        expect(rendered.getByText('150 $')).toBeInTheDocument();
        expect(rendered.getAllByText('Для дома')[0]).toBeInTheDocument();
        expect(rendered.getByAltText('lamp')).toBeInTheDocument();
    });

    it('should render ProductCard for electronics', () => {
        const rendered = render(<MainPage />);

         fireEvent.click(rendered.getAllByText('Электроника')[0]);

        expect(rendered.getByText('Iphone')).toBeInTheDocument();
        expect(rendered.getByText('Iphone_desc')).toBeInTheDocument();
        expect(rendered.getByText('999 $')).toBeInTheDocument();
        expect(rendered.getAllByText('Электроника')[0]).toBeInTheDocument();
        expect(rendered.getByAltText('Iphone')).toBeInTheDocument();
    });

});