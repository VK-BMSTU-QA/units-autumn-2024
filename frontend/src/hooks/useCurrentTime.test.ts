import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from './useCurrentTime';
describe('useCurrentTime Hook', () => {
    beforeAll(() => {
        jest.useFakeTimers();
    });
    afterAll(() => {
        jest.useRealTimers();
    });
    it('должно правильно отображаться время', () => {
        const { result } = renderHook(() => useCurrentTime());
        expect(result.current).toMatch(/^\d{2}:\d{2}:\d{2}$/);
    });
    it('должно быть возвращено текущее время', () => {
        const { result } = renderHook(() => useCurrentTime());
        const currentTime = new Date().toLocaleTimeString('ru-RU');
        expect(result.current).toBe(currentTime);
    });
    it('следует обновлять время каждую секунду', () => {
        const { result } = renderHook(() => useCurrentTime());
        const initialTime = result.current;
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        expect(result.current).not.toBe(initialTime);
    });
});