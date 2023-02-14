package uk.ac.bham.teamproject.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import uk.ac.bham.teamproject.domain.Authority;

/**
 * Spring Data JPA repository for the {@link Authority} entity.
 */
public interface AuthorityRepository extends JpaRepository<Authority, String> {}
