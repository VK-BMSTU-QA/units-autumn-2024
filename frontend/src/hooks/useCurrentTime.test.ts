import { useCurrentTime } from './useCurrentTime';
import { act, renderHook } from '@testing-library/react';

jest.useFakeTimers();
afterEach(jest.clearAllMocks);

describe('useCurrentTime test', () => {
    it('should return initial time in format of locale time string', () => {
        const mockDateLocaleString = 'date locale';
        const mockDateLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue(mockDateLocaleString);

        const { result } = renderHook(useCurrentTime);

        expect(mockDateLocale).toBeCalledTimes(1);
        expect(result.current).toBe(mockDateLocaleString);
    });

    it('should increment current time after one second', () => {
        const intervalPeriod = 1000;
        const mockDateLocaleString = 'date locale';
        const updatedMockDateLocaleString = 'new date locale';

        let mockDateLocale = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue(mockDateLocaleString);

        setTimeout(() => {
            mockDateLocale = mockDateLocale.mockReturnValue(
                updatedMockDateLocaleString
            );
        }, intervalPeriod);

        const { result } = renderHook(useCurrentTime);

        expect(result.current).toBe(mockDateLocaleString);

        act(() => {
            jest.advanceTimersByTime(intervalPeriod);
        });

        expect(result.current).toBe(updatedMockDateLocaleString);
    });
});
