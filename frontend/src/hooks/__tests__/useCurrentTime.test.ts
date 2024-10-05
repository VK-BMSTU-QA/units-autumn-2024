import { renderHook, act } from '@testing-library/react-hooks';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime', () => {
  beforeEach(() => {
    jest.useFakeTimers();
  });

  afterEach(() => {
    jest.clearAllTimers();
    jest.useRealTimers();
  });

  test('возвращает текущее время и обновляется каждую секунду', () => {
    const { result } = renderHook(() => useCurrentTime());

    const initialTime = result.current;

    act(() => {
      jest.advanceTimersByTime(1000);
    });

    expect(result.current).not.toBe(initialTime);
  });

  test('очищает интервал при размонтировании', () => {
    const { unmount } = renderHook(() => useCurrentTime());

    expect(jest.getTimerCount()).toBe(1);

    unmount();

    expect(jest.getTimerCount()).toBe(0);
  });
});
