import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';
jest.useFakeTimers(); 
describe('useCurrentTime hook', () => {
    it('should return the initial current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        const initialTime = new Date().toLocaleTimeString('ru-RU');
        expect(result.current).toBe(initialTime);
    });

    it('should update the time every second', () => {
        const { result } = renderHook(() => useCurrentTime());
        act(() => {
            jest.advanceTimersByTime(1000);
        });
        const updatedTime = new Date().toLocaleTimeString('ru-RU');
        expect(result.current).toBe(updatedTime);
    });

    it('should clear the interval when unmounted', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');
        const { unmount } = renderHook(() => useCurrentTime());
        unmount();
        expect(clearIntervalSpy).toHaveBeenCalledTimes(1);

        clearIntervalSpy.mockRestore();
    });
});
