# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template='Hello, <name>!'):
    new_template = template.replace("<name>", f"{name}")
    return new_template


def force(mass, body="earth"):
    celestial_bodies = {"sun": 274,
                        "jupiter": 24.92,
                        "neptune": 11.15,
                        "saturn": 10.44,
                        "earth": 9.798,
                        "uranus": 8.87,
                        "venus": 8.87,
                        "mars": 3.71,
                        "mercury": 3.7,
                        "moon": 1.62,
                        "pluto": 0.58}
    if body in celestial_bodies:
        gravity = celestial_bodies[body]
        gravity = "{:.1f}".format(gravity)
    force = mass * float(gravity)

    return force


def pull(m1, m2, d):
    g = 6.674 * 10 ** -11
    pull = g*((m1 * m2)/d**2)
    return pull


res = pull(800, 1500, 3)
print(res)
