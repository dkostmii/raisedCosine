from matplotlib import pyplot

# data generators
from numpy import linspace
from numpy import zeros
from numpy import meshgrid

# data operations
from numpy import concatenate
from numpy import take
from numpy import roll
from numpy import arange
from numpy import average

# functions
from numpy import sinc
from numpy import exp
from math import floor

# constants
from numpy import pi


# convert sinc to signal function representation
def sinct(t, f):
    # sinc from numpy is normalized with factor pi
    return sinc(2 * f * t / pi)


# returns (y.shape[0] + 1) sized array
def median_modify(y):
    if (y.shape[0]) % 2 == 0:
        # there is no median, so take the average
        first_middle = y[int(y.shape[0] / 2) - 1]
        second_middle = y[int(y.shape[0] / 2)]
        avg = (first_middle + second_middle) / 2

        first_chunk = y[:int(y.shape[0] / 2)]
        second_chunk = y[int(y.shape[0] / 2):]

        modified = concatenate([first_chunk, [avg], second_chunk])
    else:
        # there is median, so duplicate it
        median = y[int(floor(y.shape[0] / 2))]
        first_chunk = y[:int(floor(y.shape[0] / 2))]
        second_chunk = y[int(floor(y.shape[0] / 2)):]

        modified = concatenate([first_chunk, [median], second_chunk])

    return modified


# takes the average of each pair of terms
# returns (y.shape[0] - 1) sized array
def neighbour_average(y):
    rolled = roll(y, -1)
    shifted_y = take(y, arange(y.shape[0])[:-1])
    shifted_rolled = take(rolled, arange(rolled.shape[0])[:-1])

    avg = (shifted_y + shifted_rolled) / 2
    return avg


# takes a - initial state, tt - time range
# returns z as initial state (a) progression
def indentity_boundary(a, tt):
    result = zeros([a.shape[0], tt.shape[0]])
    result[0] = a
    for i in range(1, tt.shape[0]):
        result[i] = neighbour_average(median_modify(result[i - 1]))

    return result


# applies sinct to initial state and returns it's progression
def sinct_boundary(t, amplitude, f, tt):
    values = sinct(t, f)
    # normalize the function values
    avg = average(values)

    y = amplitude * (values - avg)
    result = indentity_boundary(y, tt)
    # return both the result and the average term to compensate normalization
    return result, avg


def samplingfrequency(val_range, samples):
    return samples / val_range


def plot_distribution(samples, start, end, freq):
    sampling_freq = samplingfrequency(end - start, samples)
    domain_freq = freq
    amplitude = 2

    tt_end = 1

    alpha = 0.01

    if tt_end < 0:
        raise Exception("tt_end must be positive")

    a = linspace(start, end, samples)
    tt = linspace(0, tt_end, samples)
    fun = (lambda t: amplitude * sinct(t, domain_freq))

    x, y = meshgrid(a, tt)

    # sinct_boundary normalizes the function by average value
    funb, avg = sinct_boundary(a, amplitude, domain_freq, tt)
    # so we need to add that term to final result
    zb = funb * exp(-alpha * ((2 * pi * domain_freq) ** 2) * y) + avg

    # simple exponent distribution
    z = fun(x) * exp(-alpha * y)

    print("Sampling frequency: " + str(sampling_freq))

    fig = pyplot.figure(figsize=(6, 6))

    # full solution plot
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.set_xlim3d(start, end)
    ax.set_ylim3d(0, tt_end)

    ax.plot_wireframe(x, y, zb, color='red')

    # simple exponent distribution plot
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.set_xlim3d(start, end)
    ax.set_ylim3d(0, tt_end)

    ax.plot_wireframe(x, y, z)

    pyplot.show()


def main():
    samples = 40
    start = -2
    end = 2

    plot_distribution(samples, start, end, 2)


if __name__ == "__main__":
    main()
