import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime } from '../../hooks';
import { updateCategories } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../utils/updateCategories.ts', () => ({
    updateCategories: jest.fn(),
}));

jest.mock('../../hooks/useCurrentTime.ts', () => ({
    useCurrentTime: () => '00:00:00',
}));

describe('Main page test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('updates the category when you click on it', () => {
        (updateCategories as jest.Mock).mockReturnValue(['Электроника'])

        const rendered = render(<MainPage />);
        const categoryButton = rendered.getAllByText('Электроника')[0];

        expect(updateCategories).toHaveBeenCalledTimes(0);
        fireEvent.click(categoryButton);
        expect(updateCategories).toHaveBeenCalledTimes(1);
        fireEvent.click(categoryButton);
        expect(updateCategories).toHaveBeenCalledTimes(2);
    });
});