import { UnstyledButton } from '@mantine/core';
import {
  IconBulb,
  IconCheckbox,
  IconUser,
  IconBrandInstagram,
  IconPencil,
  IconStack2,
  IconFilePlus
} from '@tabler/icons-react';
import classes from './Navbar.module.css';
import { Link } from 'react-router-dom';
import metrotest from '../../../../../public/metrotest.png';

const links = [
  { icon: IconUser, label: 'Авторизация', href: '/login' },
  { icon: IconStack2, label: 'КПП', href: '/kpps' },
  { icon: IconCheckbox, label: 'Задачи', href: '/tasks' },
  { icon: IconBulb, label: 'Создать задачу', href: '/createtask' },
  { icon: IconFilePlus, label: 'Cоздать КПП', href: '/createkpp' },
  { icon: IconBrandInstagram, label: 'Мой профиль', href: '/profile' },
  { icon: IconPencil, label: 'Изменить профиль', href: '/profileform' }
];

export const Navbar = () => {
  const mainLinks = links.map((link) => (
    <Link className={classes.mainLinkInner} to={link.href}>
      <UnstyledButton key={link.label} className={classes.mainLink}>
        <link.icon size={20} className={classes.mainLinkIcon} stroke={1.5} />
        <span>{link.label}</span>
      </UnstyledButton>
    </Link>
  ));

  return (
    <>
      <div className={classes.section}>
        <img className='logo' src={metrotest} alt="Логотип" />
      </div>

      <div className={classes.section}>
        <div className={classes.mainLinks}>{mainLinks}</div>
      </div>
    </>
  );
};
