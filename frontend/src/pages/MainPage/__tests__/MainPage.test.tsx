import React, { useState } from 'react';
import '@testing-library/jest-dom';
import { render, screen, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';

describe('MainPage', () => {

    beforeEach(() => {
        jest.spyOn(global.Date, 'now').mockImplementation(() => new Date('2023-10-01T12:00:00Z').getTime());
    });

    afterEach(() => {
        jest.restoreAllMocks();
    });

    it('должен отобразить заголовок и текущее время', () => {
        render(<MainPage />);

        expect(screen.getByText('VK Маркет')).toBeInTheDocument();
        const timeRegex = /\d{2}:\d{2}:\d{2}/;
        expect(screen.getByText(timeRegex)).toBeInTheDocument();
    });

    it('должен отобразить продукты с помощью компонента ProductCard', () => {
        render(<MainPage />);

        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Костюм гуся')).toBeInTheDocument();
    });

    it('должен обновлять выбранные категории при нажатии на категорию', () => {

        render(<MainPage />);

        const categoryButton = screen.getByText('Электроника', { selector: '.categories__badge' });
        fireEvent.click(categoryButton);

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
