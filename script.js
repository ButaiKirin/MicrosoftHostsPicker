document.addEventListener('DOMContentLoaded', () => {
    const features = document.querySelectorAll('.feature');
    const quickStart = document.querySelector('.quick-start');
    
    // 计算特性卡片动画的总持续时间
    const lastFeatureDelay = 0.6; // 最后一个特性卡片的延迟
    const featureAnimationDuration = 0.6; // 每个特性卡片的动画持续时间
    const totalFeatureAnimationTime = lastFeatureDelay + featureAnimationDuration;


    const zhBtn = document.getElementById('zh-btn');
    const enBtn = document.getElementById('en-btn');

    function setLanguage(lang) {
        document.querySelectorAll('[data-en]').forEach(elem => {
            elem.textContent = elem.getAttribute(`data-${lang}`);
        });
        
        if (lang === 'en') {
            zhBtn.classList.remove('active');
            enBtn.classList.add('active');
            document.documentElement.lang = 'en';
        } else {
            enBtn.classList.remove('active');
            zhBtn.classList.add('active');
            document.documentElement.lang = 'zh-CN';
        }
    }

    zhBtn.addEventListener('click', () => setLanguage('zh'));
    enBtn.addEventListener('click', () => setLanguage('en'));

    // 自动检测浏览器语言
    const userLang = navigator.language || navigator.userLanguage;
    setLanguage(userLang.startsWith('zh') ? 'zh' : 'en');

    // 设置版权年份
    const copyrightYearsSpan = document.getElementById('copyright-years');
    const startYear = 2021;
    const currentYear = new Date().getFullYear();
    copyrightYearsSpan.textContent = startYear === currentYear ? startYear : `${startYear}-${currentYear}`;

    // 获取 GitHub star 数量
    fetch('https://api.github.com/repos/ButaiKirin/MicrosoftHostsPicker')
        .then(response => response.json())
        .then(data => {
            const starCount = document.getElementById('star-count');
            starCount.textContent = data.stargazers_count;
        })
        .catch(error => console.error('Error fetching GitHub stats:', error));
});
