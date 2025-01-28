from time import time

def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

def typingSpeed(iprompt, stime, etime):
    global time
    global iwords

    iwords = iprompt.split()
    twords = len(iwords)
    speed = twords / time

    return speed

def timeElapsed(stime, etime):
    time = etime - stime

    return time

if __name__ == '__main__':
    prompt = "As human beings, it is our basic duty to care for the planet that we call our home. The Earth provides us with all the basic things that are needed for our survival. Nut, we greedy humans have exploited its resources to such an extent that even the most essentials are not available to some people. Being responsible inhabitants of this planet, we must take some measures to reverse the damage caused to our planet. It has seen a lot of exploitation. We have been cutting trees recklessly for our use. For every tree lost, the Earth loses a part of itself. We must plant as many trees as we can in our limited lifetimes, to bring the previous lush green forests back to life. If we can all plant a sapling each, every year then, the Earth will be filled with nearly 7 billion trees in one year."
    print("Type this:- '", prompt, "'")

    input("press ENTER when you are ready!")

    stime = time()
    iprompt = input()
    etime = time()

    time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt)

    print("Total Time elapsed : ", time, "s")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", errors, "errors")