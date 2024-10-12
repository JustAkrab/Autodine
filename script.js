function smoothScroll() {
    const totalHeight = document.body.scrollHeight;
    const viewportHeight = window.innerHeight;
    const duration = 5000; // Total duration of the scroll in milliseconds

    function scrollDown(startTime) {
        const currentTime = performance.now();
        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        const scrollPosition = progress * (totalHeight - viewportHeight);

        window.scrollTo(0, scrollPosition);

        if (progress < 1) {
            requestAnimationFrame(() => scrollDown(startTime));
        } else {
            setTimeout(() => {
                const startTimeUp = performance.now();
                scrollUp(startTimeUp);
            }, 1000); // Wait for 1 second before scrolling up
        }
    }

    function scrollUp(startTime) {
        const currentTime = performance.now();
        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        const scrollPosition = (1 - progress) * (totalHeight - viewportHeight);

        window.scrollTo(0, scrollPosition);

        if (progress < 1) {
            requestAnimationFrame(() => scrollUp(startTime));
        } else {
            setTimeout(() => {
                const startTimeDown = performance.now();
                scrollDown(startTimeDown);
            }, 1000); // Wait for 1 second before scrolling down again
        }
    }

    const startTimeDown = performance.now();
    scrollDown(startTimeDown);
}

async function highlightCards(){
    try{

        smoothScroll();

        console.log('Fetching orders');
        // const response = await fetch('https://');
        // const data = await response.json();
        const data = {
            ORDER: {
                "Burger": { "Cheese": 2, "Tomato":2 },
                "Caesar Salad": { "Croutons":  2}
            }
        };

        const orders = data.ORDER;

        for (const[foodItem, modifications] of Object.entries(orders)){
            console.log(`Processing food item: ${foodItem}`);
            const card = document.querySelector(`#item-${foodItem.replace(/\s+/g, '-')}`);
            if (card){
                console.log(`Found card for food item: ${foodItem}`);
                const parentCard = card.parentElement;
                parentCard.style.transform = 'scale(1.1)';
                parentCard.style.transition = 'transform 0.4s';
                


                for (const[modification,value] of Object.entries(modifications)){
                    console.log(`Highlighting modification: ${modification}`);
                    const modificationElement = parentCard.querySelector(`.mod-${modification}`);
                    if (modificationElement){
                        modificationElement.style.backgroundColor = 'lightblue';
                    } else {
                        console.log(`Modification not found: ${modification}`);
                    }

                }

                setTimeout(() => {
                    parentCard.style.transform = 'scale(1)';

                    for (const[modification,value] of Object.entries(modifications)){
                        const modificationElement = parentCard.querySelector(`.mod-${modification}`);
                        if (modificationElement){
                            modificationElement.style.backgroundColor = '';
                        }
                    }

                }, 1000);
            } else {
                console.log(`Card not found for food item: ${foodItem}`);
            }
        }
    }catch(error){
        console.error('Error fetching orders', error);
    }
}

highlightCards();

